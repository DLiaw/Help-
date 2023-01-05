import React, { useState, useEffect } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import LoginForm from './components/auth/LoginForm';
import SignUpForm from './components/auth/SignUpForm';
import NavBar from './components/Navbar/NavBar';
import { authenticate } from './store/session';
import LandingPage from '../src/components/LandingPage';
import BusinessForm from '../src/components/NewBusinessPage';
import EditBusinessForm from './components/EditBusinessPage';
import BusinessDetail from './components/BusinessDetail';
import RedNavBar from './components/RedNavBar/RedNavBar';
import CreateReview from '../src/components/NewReviewPage';
import Footer from './components/Footer';
import './index.css'

function App() {
  const [loaded, setLoaded] = useState(false);
  const dispatch = useDispatch();

  useEffect(() => {
    (async () => {
      await dispatch(authenticate());
      setLoaded(true);
    })();
  }, [dispatch]);

  if (!loaded) {
    return null;
  }

  return (
    <BrowserRouter>

      <Switch>
        <Route path='/' exact={true}>
          <NavBar />
          <LandingPage />
        </Route>
        <Route path='/login' exact={true}>
          <RedNavBar />
          <LoginForm />
          <Footer />
        </Route>
        <Route path='/sign-up' exact={true}>
          <RedNavBar />
          <SignUpForm />
          <Footer />
        </Route>
        <Route path='/business/new' exact={true}>
          <RedNavBar />
          <BusinessForm />
          <Footer />
        </Route>
        <Route path='/business/:id/edit' exact={true}>
          <RedNavBar />
          <EditBusinessForm />
          <Footer />
        </Route>
        <Route path='/business/:id' exact={true}>
          <BusinessDetail />
        </Route>
        <Route path='/business/:id/review' exact={true}>
          <RedNavBar />
          <CreateReview />
          <Footer />
        </Route>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
