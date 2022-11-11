import React from 'react'
import {Link} from 'react-router-dom'

const Header = () => {
  return (
    <div>
        <Link to={'/homepage'}>Homepage</Link>
        <span> | </span>
        <Link to={'/'}>Login</Link>
    </div>
  )
}

export default Header