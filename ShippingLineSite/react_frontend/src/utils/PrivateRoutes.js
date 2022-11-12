import { Navigate, Outlet } from "react-router-dom";


import React from 'react'

const PrivateRoutes = () => {
    let isAuth = {'token': false}

    
  return (
    isAuth.token ? <Outlet /> : <Navigate to='login'/>
  )

}

export default PrivateRoutes;