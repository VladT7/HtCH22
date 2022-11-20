// import { Button } from "@mui/material";
// import { Link} from "react-router-dom";
// import './Home.css';

// export default function Home (){

//     return (
//         <div>
//           <div className="d-md-flex">

//           <Link to="/signup">
//             <Button> Sign Up</Button>
//           </Link>
//           <Link to="/vision">
//             <Button>Try it out!</Button>
//           </Link>
//           </div>
//         </div>
//     );
// }
// import "./App.css";
import "./Home.css";
import rectangle15 from "../assets/rectangle15.svg";
import TypographyDisplay from "../components/TypographyDisplay";
import Button1 from "../components/Button1";
import TypographyDisplay1 from "../components/TypographyDisplay1";
import Image from "../components/Image";
import Button from "../components/Button";
const Home = () => {
  const propsData = {
    typographyDisplay1: {
      display2: "fiberr",
    },
    typographyDisplay: {
      display4: "make better choices",
    },
    image: {
      baseImage: {
        text: "Fluid",
      },
    },
    button: {
      button: {
        text: "Log In",
      },
    },
    button1: {
      button: {
        text: "Try it out!",
      },
    },
  };
  return (
    <div className="home">
      <div className="cat-absolute-container">
        <TypographyDisplay1
          className="typography-display-1-instance-1"
          {...propsData.typographyDisplay1}
        />
        <TypographyDisplay
          className="typography-display-instance-1"
          {...propsData.typographyDisplay}
        />
        <Image
          className="image-instance-1"
          {...propsData.image}
        />
        <div className="flex-container">
          <Button
            className="button-instance-3"
            {...propsData.button}
          />
          <Button1
            className="button-1-instance-1"
            {...propsData.button1}
          />
        </div>
      </div>
      <img
        className="rectangle-15"
        src={rectangle15}
      />
    </div>
  );
};
export default Home;
