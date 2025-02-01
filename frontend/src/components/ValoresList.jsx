import React from 'react';
import { desactivarValor } from '../api/axios';
import './ValoresList.css';

const ValoresList = ({ valores, onEdit, onValoresChange }) => {
  const handleDesactivar = async (id) => {
    try {
      await desactivarValor(id);
      onValoresChange();
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