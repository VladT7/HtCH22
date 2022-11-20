import "./Image.css";
import BaseImage from "./BaseImage";
const Image = (props) => {
  return (
    <div className={`image ${props.className || ""}`}>
      <BaseImage className="base-image-instance-1" {...props.baseImage} />
    </div>
  );
};
export default Image;
