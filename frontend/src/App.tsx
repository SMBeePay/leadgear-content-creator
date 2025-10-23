import { Routes, Route, Navigate } from 'react-router-dom'
import { useAuthStore } from './stores/authStore'
import Layout from './components/Layout'
import LoginPage from './pages/LoginPage'
import RegisterPage from './pages/RegisterPage'
import HomePage from './pages/HomePage'
import ProjectListPage from './pages/ProjectListPage'
import ProjectDetailPage from './pages/ProjectDetailPage'
import KeywordResearchPage from './pages/KeywordResearchPage'
import ContentEditorPage from './pages/ContentEditorPage'

function App() {
  const { isAuthenticated } = useAuthStore()

  return (
    <Routes>
      {/* Public routes */}
      <Route path="/login" element={!isAuthenticated ? <LoginPage /> : <Navigate to="/" />} />
      <Route path="/register" element={!isAuthenticated ? <RegisterPage /> : <Navigate to="/" />} />

      {/* Protected routes */}
      <Route path="/" element={isAuthenticated ? <Layout /> : <Navigate to="/login" />}>
        <Route index element={<HomePage />} />
        <Route path="projects" element={<ProjectListPage />} />
        <Route path="projects/:projectId" element={<ProjectDetailPage />} />
        <Route path="projects/:projectId/content/new" element={<KeywordResearchPage />} />
        <Route path="content/:contentId/edit" element={<ContentEditorPage />} />
      </Route>

      {/* Catch all */}
      <Route path="*" element={<Navigate to="/" />} />
    </Routes>
  )
}

export default App
