import { Button } from "@mui/material";
import { Link} from "react-router-dom";
import './Home.css';

export default function Home (){

    return (
        <div>
          <div className="d-md-flex">

          <Link to="/signup">
            <Button> Sign Up</Button>
          </Link>
          <Link to="/vision">
            <Button>Try it out!</Button>
          </Link>
          </div>
        </div>
    );
}
