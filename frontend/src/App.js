import React, { useState, useEffect } from 'react';
import ValoresList from './components/ValoresList';
import ValorForm from './components/ValorForm';
import { getValores } from './api/axios';
import './App.css';

const App = () => {
  const [valorToEdit, setValorToEdit] = useState(null);
  const [valores, setValores] = useState([]);

  const loadValores = async () => {
    try {
      const response = await getValores();
      setValores(response.data);
    } catch (error) {
      console.error('Error loading valores:', error);
    }
  };

  useEffect(() => {
    loadValores();
  }, []);

  const handleEdit = (valor) => {
    setValorToEdit(valor);
  };

  const handleSave = () => {
    loadValores(); // Recargamos los datos después de guardar
    setValorToEdit(null);
  };

  return (
    <div className="app">
      <h1>Gestión de Valores</h1>
      <ValorForm valorToEdit={valorToEdit} onSave={handleSave} />
      <ValoresList valores={valores} onEdit={handleEdit} onValoresChange={loadValores} />
    </div>
  );
};

export default App;