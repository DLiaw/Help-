
import React, { useState, useEffect } from 'react';
import { useSelector } from 'react-redux';
import { NavLink } from 'react-router-dom';
import LogoutButton from '../auth/LogoutButton';
import './Navbar.css'

const Navbar = ({ business }) => {
    const user = useSelector(state => state.session.user)
    const [showMenu, setShowMenu] = useState(false)
    const [review, setReview] = useState(false)
    const reviews = Object.values(business.reviews)

    useEffect(() => {
        const reviewFound = reviews.find(review => {
            return user && review.user_id == user.id
        })
        if (reviewFound == undefined) setReview(true)
    }, [review])


    const openMenu = () => {
        if (showMenu) return
        setShowMenu(true)
    }

    useEffect(() => {
        if (!showMenu) return;

        const closeMenu = () => {
            setShowMenu(false);
        };

        document.addEventListener('click', closeMenu);

        return () => document.removeEventListener("click", closeMenu);
    }, [showMenu]);

    return (
        <div>
            {!user && <div className='navbar-div-business-page'>
                <nav className='navbar-main-business-page' >
                    <div>
                        <NavLink to='/' style={{ paddingLeft: '10px', display: 'flex', flexDirection: 'row', textDecoration: 'none' }} exact={true} activeClassName='active'>
                            <img style={{ height: "50px", width: "50px", objectFit: "scale-down" }} alt='home-button' src='https://logos-world.net/wp-content/uploads/2020/12/Yelp-Logo-700x394.png'></img>
                            <p id='help-business-page'>Help!</p>
                        </NavLink>
                    </div>
                    <div className='login-signup-business-page'>
                        <div style={{ paddingTop: '25px' }}>
                            <NavLink to="/sign-up" style={{ color: 'black', textDecoration: 'none' }}>For Business</NavLink>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                        </div>
                        <div style={{ paddingTop: '25px' }}>
                            <NavLink to='/sign-up' style={{ color: 'black', textDecoration: 'none' }}>Write a Review</NavLink>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                        </div>
                        <div className='login-div-business-page'>
                            <NavLink to='/login' className='login' exact={true} activeClassName='active'>
                                Login
                            </NavLink>
                        </div>
                        <div>&nbsp;&nbsp;&nbsp;&nbsp;</div>
                        <div className='signup-div-business-page'>
                            <NavLink className='sign-up' to='/sign-up' exact={true} activeClassName='active'>
                                Sign Up
                            </NavLink>
                        </div>
                    </div>
                </nav>
            </div>}
            {
                user && <div className='navbar-div-business-page'>
                    <nav className='navbar-main-business-page' >
                        <div>
                            <NavLink to='/' style={{ display: 'flex', flexDirection: 'row', textDecoration: 'none' }} exact={true} activeClassName='active'>
                                <img style={{ height: "50px", width: "50px", objectFit: "scale-down" }} alt='home-button' src='https://logos-world.net/wp-content/uploads/2020/12/Yelp-Logo-700x394.png'></img>
                                <p id='help-business-page'>Help!</p>
                            </NavLink>
                        </div>
                        <div className='login-signup-business-page'>
                            <div style={{ paddingTop: '25px' }}>
                                <NavLink to="/business/new" style={{ color: 'black', textDecoration: 'none' }}>For Business</NavLink>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                            </div>
                            {review && user && user.id !== business.owner_id && < div style={{ paddingTop: '25px' }}>
                                <NavLink to={`/business/${business.id}/review`} style={{ color: 'black', textDecoration: 'none' }}>Write a Review</NavLink>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                            </div>}
                            <div className='profile-button-business-page' onClick={openMenu}>
                                <i style={{ paddingTop: '10px', fontSize: '35px', color: "grey" }} className="fa-solid fa-circle-user" />
                                {showMenu &&
                                    <LogoutButton />
                                }
                            </div>
                        </div>
                    </nav>
                </div >
            }
        </div >
    );
}

export default Navbar;
