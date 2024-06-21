import './App.css';
import fonts from './cssModules/fonts.module.css';

import Home from './pages/Home.tsx';

function App() {
  return (
    <div className={fonts.latoRegular}>
      <Home />
    </div>
  );
}

export default App
