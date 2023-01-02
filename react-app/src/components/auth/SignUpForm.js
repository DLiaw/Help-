import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux'
import * as sessionActions from '../../store/session'
import { Redirect } from 'react-router-dom';
import { signUp } from '../../store/session';
import { login } from '../../store/session'
import image from './signup.png'
import './auth.css'

const SignUpForm = () => {
  const [errors, setErrors] = useState([]);
  const [email, setEmail] = useState('');
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [password, setPassword] = useState('');
  const user = useSelector(state => state.session.user);
  const dispatch = useDispatch();

  const onSignUp = async (e) => {
    e.preventDefault();
    setErrors([]);
    const data = await dispatch(signUp(firstName, lastName, email, password));
    if (data) {
      setErrors(data)
    }
  }


  const handleDemo = (e) => {
    e.preventDefault()
    return dispatch(login("demo@gmail.com", 'password'))
  };


  if (user) {
    return <Redirect to='/' />;
  }

  return (
    <div className='div-signup'>
      <form className='signup-form' onSubmit={onSignUp}>
        <div>
          {errors.map((error, ind) => (
            <div key={ind}>{error}</div>
          ))}
        </div>
        <div>
          <div className='signup-info'><p id='p1'>Sign Up for Help</p></div>
          <div className='signup-info'><p id='p2'>Connect with great local businesses</p></div>
          <div className='signup-info'><p id='p3'>By continuing, you agree to Help’s Terms of Service and acknowledge Help’s Privacy Policy.</p></div>
          <div className='first-last'>
            <input id='fullname'
              type='text'
              name='firstname'
              value={firstName}
              onChange={(e) => setFirstName(e.target.value)}
              required
              placeholder='First Name'
            ></input>
            <div>&nbsp;</div>
            <input id='fullname'
              type='text'
              name='lastname'
              onChange={(e) => setLastName(e.target.value)}
              value={lastName}
              required
              placeholder='Last Name'
            ></input>
          </div>
        </div>
        <div>
          <input
            className='signup-email-password'
            type='text'
            name='email'
            onChange={(e) => setEmail(e.target.value)}
            value={email}
            required
            placeholder='Email'
          ></input>
        </div>
        <div>
          <input
            className='signup-email-password'
            type='password'
            name='password'
            onChange={(e) => setPassword(e.target.value)}
            value={password}
            required
            placeholder='Password'
          ></input>
        </div>
        <button className='signup-button' type='submit'>Sign Up</button>
        <div className='or-div'>&nbsp;&nbsp;OR&nbsp;&nbsp;</div>
        <button className="signup-button" onClick={handleDemo}>Demo User</button>
      </form>
      <div>
        <img alt='signup' src={image}></img>
      </div>
    </div>
  );
};

export default SignUpForm;
