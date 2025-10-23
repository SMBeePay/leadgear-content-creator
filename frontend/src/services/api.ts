import axios from 'axios'
import { useAuthStore } from '../stores/authStore'

// Get API URL from Vite environment variable
const API_URL = (import.meta as any).env.VITE_API_URL || 'http://localhost:8000'

// Create axios instance
export const api = axios.create({
  baseURL: `${API_URL}/api`,
  headers: {
    'Content-Type': 'application/json',
  },
})

// Request interceptor to add auth token
api.interceptors.request.use(
  (config) => {
    const token = useAuthStore.getState().token
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

// Response interceptor to handle errors
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // Unauthorized - clear auth and redirect to login
      useAuthStore.getState().logout()
      window.location.href = '/login'
    }
    return Promise.reject(error)
  }
)

// Auth API
export const authApi = {
  register: async (email: string, password: string, fullName?: string) => {
    const response = await api.post('/auth/register', {
      email,
      password,
      full_name: fullName,
    })
    return response.data
  },

  login: async (email: string, password: string) => {
    const response = await api.post('/auth/login', { email, password })
    return response.data
  },

  getCurrentUser: async () => {
    const response = await api.get('/auth/me')
    return response.data
  },
}

// Projects API
export const projectsApi = {
  list: async () => {
    const response = await api.get('/projects')
    return response.data
  },

  get: async (id: string) => {
    const response = await api.get(`/projects/${id}`)
    return response.data
  },

  create: async (data: any) => {
    const response = await api.post('/projects', data)
    return response.data
  },

  update: async (id: string, data: any) => {
    const response = await api.patch(`/projects/${id}`, data)
    return response.data
  },

  delete: async (id: string) => {
    await api.delete(`/projects/${id}`)
  },
}

// Keywords API
export const keywordsApi = {
  research: async (data: any) => {
    const response = await api.post('/keywords/research', data)
    return response.data
  },
}

// SERP API
export const serpApi = {
  analyze: async (data: any) => {
    const response = await api.post('/serp/analyze', data)
    return response.data
  },
}

// Content API
export const contentApi = {
  get: async (id: string) => {
    const response = await api.get(`/content/${id}`)
    return response.data
  },

  update: async (id: string, data: any) => {
    const response = await api.patch(`/content/${id}`, data)
    return response.data
  },

  generate: async (briefId: string) => {
    const response = await api.post('/content/generate', { brief_id: briefId })
    return response.data
  },

  improve: async (contentId: string, data: any) => {
    const response = await api.post(`/content/${contentId}/improve`, data)
    return response.data
  },

  validate: async (contentId: string) => {
    const response = await api.post(`/content/${contentId}/validate`)
    return response.data
  },
}

// Briefs API
export const briefsApi = {
  generate: async (data: any) => {
    const response = await api.post('/briefs/generate', data)
    return response.data
  },

  get: async (id: string) => {
    const response = await api.get(`/briefs/${id}`)
    return response.data
  },

  update: async (id: string, data: any) => {
    const response = await api.patch(`/briefs/${id}`, data)
    return response.data
  },

  approve: async (id: string) => {
    const response = await api.post(`/briefs/${id}/approve`)
    return response.data
  },
}

// Meta API
export const metaApi = {
  generate: async (data: any) => {
    const response = await api.post('/meta/generate', data)
    return response.data
  },

  suggestImages: async (content: string) => {
    const response = await api.post('/meta/images/suggest', { content })
    return response.data
  },
}

// Export API
export const exportApi = {
  toGoogleDocs: async (data: any) => {
    const response = await api.post('/export/google-docs', data)
    return response.data
  },
}
