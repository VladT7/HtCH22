import "./Button1.css";
import Button from "./Button";
const Button1 = (props) => {
  return (
    <button className={`button-1 ${props.className || ""}`}>
      <Button className="button-instance-1" {...props.button} />
    </button>
  );
};
export default Button1;
