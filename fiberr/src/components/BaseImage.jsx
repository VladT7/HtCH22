import "./BaseImage.css";
const BaseImage = (props) => {
  return (
    <div className={`base-image ${props.className || ""}`}>
      {props.text || "Fluid"}
    </div>
  );
};
export default BaseImage;
