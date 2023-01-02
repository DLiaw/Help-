
import React, { useState, useEffect } from 'react';
import { useSelector } from 'react-redux';
import { NavLink } from 'react-router-dom';
import LogoutButton from '../auth/LogoutButton';
import './NavBar.css'

const NavBar = () => {
  const user = useSelector(state => state.session.user)
  const [showMenu, setShowMenu] = useState(false)

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
      {!user && <div className='navbar-div'>
        <nav className='navbar-main' >
          <div>
            <NavLink to='/' style={{ display: 'flex', flexDirection: 'row', textDecoration: 'none' }} exact={true} activeClassName='active'>
              <img style={{ height: "50px", width: "50px", objectFit: "scale-down" }} alt='home-button' src='https://logos-world.net/wp-content/uploads/2020/12/Yelp-Logo-700x394.png'></img>
              <p id='help'>Help!</p>
            </NavLink>
          </div>
          <div className='login-signup'>
            <div style={{ paddingTop: '10px' }}>
              <NavLink to="/sign-up" style={{ color: 'white', textDecoration: 'none' }}>For Business</NavLink>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            </div>
            <div style={{ paddingTop: '10px' }}>
              <NavLink to='/sign-up' style={{ color: 'white', textDecoration: 'none' }}>Write a Review</NavLink>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            </div>
            <div className='login-div'>
              <NavLink to='/login' className='login' exact={true} activeClassName='active'>
                Login
              </NavLink>
            </div>
            <div>&nbsp;&nbsp;&nbsp;&nbsp;</div>
            <div className='signup-div'>
              <NavLink className='sign-up' to='/sign-up' exact={true} activeClassName='active'>
                Sign Up
              </NavLink>
            </div>
          </div>
        </nav>
      </div>}
      {
        user && <div className='navbar-div'>
          <nav className='navbar-main' >
            <div>
              <NavLink to='/' style={{ display: 'flex', flexDirection: 'row', textDecoration: 'none' }} exact={true} activeClassName='active'>
                <img style={{ height: "50px", width: "50px", objectFit: "scale-down" }} alt='home-button' src='https://logos-world.net/wp-content/uploads/2020/12/Yelp-Logo-700x394.png'></img>
                <p id='help'>Help!</p>
              </NavLink>
            </div>
            <div className='login-signup'>
              <div style={{ paddingTop: '10px' }}>
                <NavLink to="/business/new" style={{ color: 'white', textDecoration: 'none' }}>For Business</NavLink>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
              </div>
              <div style={{ paddingTop: '10px' }}>
                <NavLink to='/business/2' style={{ color: 'white', textDecoration: 'none' }}>Write a Review</NavLink>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
              </div>
              <div className='profile-button' onClick={openMenu}>
                <i style={{ fontSize: '35px', color: "grey" }} className="fa-solid fa-circle-user" />
                {showMenu &&
                  <LogoutButton />
                }
              </div>
            </div>
          </nav>
        </div>
      }
    </div>
  );
}

export default NavBar;
