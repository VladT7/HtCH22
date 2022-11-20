import "./TypographyDisplay.css";
const TypographyDisplay = (props) => {
  return (
    <div className={`typography-display ${props.className || ""}`}>
      <span className="display-4">
        {props.display4 || "make better choices"}
      </span>
    </div>
  );
};
export default TypographyDisplay;
