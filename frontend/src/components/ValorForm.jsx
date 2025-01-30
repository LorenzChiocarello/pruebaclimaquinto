import React, { useState, useEffect } from 'react';
import { createValor, updateValor, getTipos } from '../api/axios';
import './ValorForm.css';

const ValorForm = ({ valorToEdit, onSave }) => {
  const [tipos, setTipos] = useState([]);
  const [formData, setFormData] = useState({
    tipo_id: '',
    fecha: '',
    valor: ''
  });

  useEffect(() => {
    loadTipos();
    if (valorToEdit) {
      setFormData({
        tipo_id: valorToEdit.tipo_id,
        fecha: valorToEdit.fecha.split('T')[0],
        valor: valorToEdit.valor
      });
    }
  }, [valorToEdit]);

  const loadTipos = async () => {
    try {
      const response = await getTipos();
      setTipos(response.data);
    } catch (error) {
      console.error('Error loading tipos:', error);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      if (valorToEdit) {
        await updateValor(valorToEdit.id, formData);
      } else {
        await createValor(formData);
      }
      setFormData({ tipo_id: '', fecha: '', valor: '' });
      onSave();
    } catch (error) {
      console.error('Error saving valor:', error);
    }
  };

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  return (
    <div className="valor-form">
      <h2>{valorToEdit ? 'Editar Valor' : 'Nuevo Valor'}</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label>Tipo:</label>
          <select
            name="tipo_id"
            value={formData.tipo_id}
            onChange={handleChange}
            required
          >
            <option value="">Seleccionar tipo</option>
            {tipos.map((tipo) => (
              <option key={tipo.id} value={tipo.id}>
                {tipo.tipo}
              </option>
            ))}
          </select>
        </div>
        <div className="form-group">
          <label>Fecha:</label>
          <input
            type="date"
            name="fecha"
            value={formData.fecha}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-group">
          <label>Valor:</label>
          <input
            type="number"
            name="valor"
            value={formData.valor}
            onChange={handleChange}
            required
          />
        </div>
        <button type="submit" className="button submit">
          {valorToEdit ? 'Actualizar' : 'Guardar'}
        </button>
      </form>
    </div>
  );
};

export default ValorForm;