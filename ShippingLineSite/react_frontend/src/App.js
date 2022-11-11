import './App.css';
import HomePage from './pages/HomePage';
import LoginPage from './pages/LoginPage';
import {BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import Header from './components/Header';

function App() {
  return (
    <div className="App">

    <Router>
      <Header />
      <Routes>
        
        <Route path='/' element={<LoginPage />}></Route> 
        <Route path='/homepage' element={ <HomePage />}></Route>
      </Routes>
    </Router>
    </div>
  );
}

export default App;
