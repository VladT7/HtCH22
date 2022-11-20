import { Button } from "@mui/material";
import { Link} from "react-router-dom";


export default function Home (){

    return (
        <div>
          <div>Home</div>
          <Link to="/signup">
            <Button> Sign Up</Button>
          </Link>
        </div>
    );
}
