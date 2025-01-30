import React, { useState } from 'react';
import ValoresList from './components/ValoresList';
import ValorForm from './components/ValorForm';
import './App.css';

const App = () => {
  const [valorToEdit, setValorToEdit] = useState(null);

  const handleEdit = (valor) => {
    setValorToEdit(valor);
  };

  const handleSave = () => {
    setValorToEdit(null);
  };

  return (
    <div className="app">
      <h1>Gestión de Valores</h1>
      <ValorForm valorToEdit={valorToEdit} onSave={handleSave} />
      <ValoresList onEdit={handleEdit} />
    </div>
  );
};

export default App;