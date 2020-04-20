import React from 'react';
import {Route} from 'react-router-dom';
import Vehicle from "./map/vehiclePosition";

const BaseRouter = () => (
    <div>
        <Route exact path='/' component={Vehicle}/>
    </div>
);

export default BaseRouter;