import React from "react";
import { NavLink } from "react-router-dom";
import './rednav.css'
const RedNavBar = () => {
    return (
        <div className="red-navbar">
            <NavLink className='red-nav' to='/'>
                <img style={{ height: "40px", width: "40px", objectFit: "scale-down" }} alt='home-button' src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRIN1_XMCJHbFwkLP5-nkvYgV49yQs16ycAXg&usqp=CAU'></img>
            </NavLink>
            <NavLink className="help" to='/'>Help!</NavLink>
        </div>
    )
}

export default RedNavBar;
