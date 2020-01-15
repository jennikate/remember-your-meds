import React from 'react'
import ReactDOM from 'react-dom'
import { Switch, Route, HashRouter } from 'react-router-dom'

import ResponsiveDrawer from './components/Navbar'
import Home from './components/Home'
import Register from './components/Register'
import Login from './components/Login'
import Prescriptions from './components/Prescriptions'
import Prescription from './components/Prescription'
import Profile from './components/Profile'
import Logout from './components/Logout'
import EditProfile from './components/EditProfile'
import CreatePrescription from './components/CreatePrescription2'
import EditPrescription from './components/EditPrescription'

import EditReminder from './components/EditReminder'


//STYLES FOR OVERWRITING MATERIAL UI
import './styles/main.css'

const App = () => {


  return (
    <HashRouter>
      <ResponsiveDrawer />
      <Switch>
        <Route exact path='/' component={Home} />
        <Route exact path="/register" component={Register} />
        <Route exact path="/login" component={Login} />
        <Route exact path="/prescriptions" component={Prescriptions} />
        <Route exact path='/prescriptions/create' component={CreatePrescription} />
        <Route exact path="/prescriptions/:id" component={Prescription} />
        <Route exact path="/prescriptions/:id/edit" component={EditPrescription} />
        <Route exact path="/prescriptions/:id/edit-reminders" component={EditReminder} />
        <Route exact path='/profile' component={Profile} />
        <Route exact path='/profile/edit' component={EditProfile} />
        <Route exact path='/logout' component={Logout} />
      </Switch>
    </HashRouter>
  )
}

ReactDOM.render(
  <App />,
  document.getElementById('root')
)
