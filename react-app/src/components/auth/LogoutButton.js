import React from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { NavLink, useHistory } from 'react-router-dom';
import { logout } from '../../store/session';
import './auth.css'

const LogoutButton = () => {
  const user = useSelector(state => state.session.user)
  const history = useHistory()
  const dispatch = useDispatch()


  const onLogout = async (e) => {
    await dispatch(logout());
    history.push("/")
  };

  return (
    <div className='profile-dropdown'>
      <div style={{ borderBottom: '.5px solid grey' }} className='dropdown-info'>
        {user.first_name}&nbsp;{user.last_name.slice(0, 1)}
        <i class="fa-solid fa-user" />
      </div>
      <div style={{ borderBottom: '.5px solid grey' }} className='dropdown-info'>
        <NavLink style={{ textDecoration: 'none', color: 'grey' }} to='/business/new'>New Business</NavLink>
        <i class="fa-solid fa-store" />
      </div>
      <div className='dropdown-info'>
        <button className='logout-button' onClick={onLogout}>Logout</button>
        <i class="fa-solid fa-right-from-bracket" />
      </div>
    </div>
  );
};

export default LogoutButton;
