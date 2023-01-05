import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { NavLink, Redirect } from 'react-router-dom';
import { login } from '../../store/session';
import image from './signup.png'

const LoginForm = () => {
  const [errors, setErrors] = useState([]);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const user = useSelector(state => state.session.user);
  const dispatch = useDispatch();

  const onLogin = async (e) => {
    e.preventDefault();
    const data = await dispatch(login(email, password));
    if (data) {
      setErrors(data);
    }
  };

  const handleDemo = (e) => {
    e.preventDefault()
    return dispatch(login("demo@gmail.com", 'password'))
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  if (user) {
    return <Redirect to='/' />;
  }

  return (
    <div className='div-login'>

      <div className='login-form-div'>
        <div>
          <div className='login-messages'>
            <label>Log in to Help!</label>
          </div>
          <div className='link-signup'>
            <p>New to Help?</p> &nbsp;&nbsp;
            <NavLink style={{ textDecoration: 'none', color: 'rgb(105, 105, 255)' }} to='/sign-up'>Sign up</NavLink>
          </div>
        </div>
        <form className='login-form' onSubmit={onLogin}>
          <div>
            {errors.map((error, ind) => (
              <div key={ind}>{error}</div>
            ))}
          </div>
          <div>
            <input
              className='login-email-password'
              name='email'
              type='text'
              placeholder='Email'
              value={email}
              onChange={updateEmail}
            />
          </div>
          <div>
            <input
              className='login-email-password'
              name='password'
              type='password'
              placeholder='Password'
              value={password}
              onChange={updatePassword}
            />
            <div>
              <button className="login-button" type='submit'>Login</button>
            </div>
            <div className='or-divtwo'>&nbsp;&nbsp;OR&nbsp;&nbsp;</div>
            <button className="login-button" onClick={handleDemo}>Demo User</button>
          </div>
          <div className='link-signup-bottom'>
            <label>New to Help?</label>&nbsp;&nbsp;
            <NavLink style={{ textDecoration: 'none', color: 'rgb(105, 105, 255)' }} to='/sign-up'>Sign up</NavLink></div>
        </form>
      </div>
      <div>
        <img alt='signup' src={image}></img>
      </div>
    </div>
  );
};

export default LoginForm;
