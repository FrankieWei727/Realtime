import React, {useState} from "react";
import {Map, TileLayer, Marker, Popup} from 'react-leaflet';

const Vehicle = () => {

    const [center] = useState([51.505, -0.091]);
    const [zoom] = useState(13);
    return (
        <div>
            <Map
                style={{height: "480px", width: "100%"}}
                zoom={1}
                center={[-0.09, 51.505]}>
                <TileLayer url="http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"/>
            </Map>
        </div>
    )
};

export default Vehicle