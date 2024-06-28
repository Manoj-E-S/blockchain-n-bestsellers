import { BrowserRouter } from 'react-router-dom';
import AppRoutes from './components/routing/Routes';
import './App.css'

const App: React.FC =()=> {

  return (
    <BrowserRouter>
      <AppRoutes />
    </BrowserRouter>
  );
};

export default App;
