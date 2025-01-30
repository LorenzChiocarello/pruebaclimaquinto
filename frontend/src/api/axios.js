import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:5000'
});

export const getValores = () => api.get('/valores');
export const getValor = (id) => api.get(`/valores/${id}`);
export const createValor = (data) => api.post('/valores', data);
export const updateValor = (id, data) => api.put(`/valores/${id}`, data);
export const desactivarValor = (id) => api.put(`/valores/${id}/desactivar`);
export const getTipos = () => api.get('/tipos');