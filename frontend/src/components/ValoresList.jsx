import React, { useState, useEffect } from 'react';
import { getValores, desactivarValor } from '../api/axios';
import './ValoresList.css';

const ValoresList = ({ onEdit }) => {
  const [valores, setValores] = useState([]);

  useEffect(() => {
    loadValores();
  }, []);

  const loadValores = async () => {
    try {
      const response = await getValores();
      setValores(response.data);
    } catch (error) {
      console.error('Error loading valores:', error);
    }
  };

  const handleDesactivar = async (id) => {
    try {
      await desactivarValor(id);
      loadValores();
    } catch (error) {
      console.error('Error desactivating valor:', error);
    }
  };

  return (
    <div className="valores-list">
      <h2>Lista de Valores</h2>
      <div className="table-container">
        <table>
          <thead>
            <tr>
              <th>Tipo</th>
              <th>Fecha</th>
              <th>Valor</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            {valores.map((valor) => (
              <tr key={valor.id}>
                <td>{valor.tipo}</td>
                <td>{new Date(valor.fecha).toLocaleDateString()}</td>
                <td>{valor.valor}</td>
                <td>
                  <button
                    className="button edit"
                    onClick={() => onEdit(valor)}
                  >
                    Editar
                  </button>
                  <button
                    className="button delete"
                    onClick={() => handleDesactivar(valor.id)}
                  >
                    Desactivar
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default ValoresList;