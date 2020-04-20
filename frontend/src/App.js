import React from 'react';
import './App.css';
import {BrowserRouter as Router} from "react-router-dom";
import BaseRouter from "./routes";
import 'leaflet/dist/leaflet.css';

function App() {

    return (
        <div>
            <Router>
                <BaseRouter/>
            </Router>
        </div>
    );
}

export default App;
