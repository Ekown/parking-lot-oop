const Stepper = (props) => {
    const currentValue = props.value;

    const increment = () => {
        if (currentValue < props.max) {
            props.setCurrentValue(Number(currentValue) + 1);
        }
    };

    const decrement = () => {
        if (currentValue > props.min) {
            props.setCurrentValue(currentValue - 1);
        }
    }

    return (
        <div className="col-xl-7">
            <div className="input-group">
                <div className="input-group-prepend">
                    <button className="btn btn-outline-primary" type="button" onClick={decrement}>-</button>
                </div>
                <input type="text" className="form-control text-center" value={currentValue} disabled />
                <div className="input-group-prepend">
                    <button className="btn btn-outline-primary" type="button" onClick={increment}>+</button>
                </div>
            </div>
        </div>
    );
}

export default Stepper;