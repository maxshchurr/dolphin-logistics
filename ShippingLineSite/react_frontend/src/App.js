import './App.css';
import HomePage from './pages/HomePage';
import LoginPage from './pages/LoginPage';
import {BrowserRouter, Routes, Route} from 'react-router-dom';
import Header from './components/Header';
import PrivateRoutes from './utils/PrivateRoutes';


function App() {
  return (
    <div className="App">

    <BrowserRouter>
      <Header />
      <Routes>

        <Route element={<PrivateRoutes/> }>
          <Route element={<HomePage/>} path='/'/>
        </Route>

        <Route path="/login" element={<LoginPage />} />
        
      </Routes>
    </BrowserRouter>
    </div>
  );
}




export default App;
