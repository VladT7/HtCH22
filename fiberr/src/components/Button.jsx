import "./Button.css";
const Button = (props) => {
  return (
    <div className={`button ${props.className || ""}`}>
      <span className="text">{props.text || "Log In"}</span>
    </div>
  );
};
export default Button;
