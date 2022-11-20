import "./TypographyDisplay1.css";
const TypographyDisplay1 = (props) => {
  return (
    <div className={`typography-display-1 ${props.className || ""}`}>
      <span className="display-2">{props.display2 || "fiberr"}</span>
    </div>
  );
};
export default TypographyDisplay1;
