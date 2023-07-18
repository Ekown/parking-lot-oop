import { useEffect, useState } from "react";
import { useWizard } from "react-use-wizard";

import "./SetParkingSlotSizes.scss";
import ParkingMap from "../../common/ParkingMap/ParkingMap";
import { getParkingSlotSize } from "../../../helpers/getParkingSlotSize";

const SetParkingSlotSizes = (props) => {
    const {
        isLoading,
        isLastStep,
        isFirstStep,
        activeStep,
        stepCount,
        previousStep,
        nextStep,
        goToStep,
        handleStep,
    } = useWizard();

    const handleParkingSlotSizeChange = (rowIndex, columnIndex, cellValue) => {
        // props.updateParkingMap(rowIndex, columnIndex, cellValue);
        const previousSize = getParkingSlotSize(rowIndex, columnIndex, props.parkingSlotSizes);

        const updatedSizes = { ...props.parkingSlotSizes };

        updatedSizes[previousSize] = updatedSizes[previousSize].filter(coord => coord.rowIndex !== rowIndex || coord.columnIndex !== columnIndex)

        // Add the coordinate to the new size
        updatedSizes[cellValue] = [...updatedSizes[cellValue], { rowIndex, columnIndex }];

        props.setParkingSlotSizes(updatedSizes)
    }

    return (
        <div className="set-parking-slot-sizes">
            <div className="row">
                <h2>Set the parking slot sizes</h2>

                <div className="col-8">
                    <ParkingMap config={props.parkingMapConfig} step={activeStep} entryPoints={props.entryPoints} handleParkingSlotSizeChange={handleParkingSlotSizeChange} />
                </div>

                <div className="col-4">
                    <div className="step-nav-buttons">
                        <button onClick={() => previousStep()}>Previous</button>
                        <button onClick={() => nextStep()}>Next</button>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default SetParkingSlotSizes;