import React from 'react'
import {Link} from 'react-router-dom'


const Header = () => {
  return (
    <div className='header'>
        <Link to={'/'}>Homepage</Link>
        <span> | </span>
        <Link to={'/login'}>Login</Link>
    </div>
  )
}

export default Header