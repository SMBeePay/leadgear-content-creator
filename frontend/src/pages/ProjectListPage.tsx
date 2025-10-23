import { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import { projectsApi } from '../services/api'

interface Project {
  id: string
  name: string
  website_url: string
  content_count: number
  updated_at: string
}

export default function ProjectListPage() {
  const [projects, setProjects] = useState<Project[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')

  useEffect(() => {
    loadProjects()
  }, [])

  const loadProjects = async () => {
    try {
      const data = await projectsApi.list()
      setProjects(data)
    } catch (err: any) {
      setError('Failed to load projects')
    } finally {
      setLoading(false)
    }
  }

  if (loading) {
    return (
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="text-center">
          <div className="inline-block animate-spin rounded-full h-8 w-8 border-b-2 border-primary-600"></div>
          <p className="mt-2 text-gray-600">Loading projects...</p>
        </div>
      </div>
    )
  }

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <div className="flex justify-between items-center mb-8">
        <h1 className="text-3xl font-bold text-gray-900">Projects</h1>
        <Link
          to="/projects/new"
          className="bg-primary-600 hover:bg-primary-700 text-white px-4 py-2 rounded-md font-medium"
        >
          + New Project
        </Link>
      </div>

      {error && (
        <div className="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded mb-6">
          {error}
        </div>
      )}

      {projects.length === 0 ? (
        <div className="bg-white rounded-lg shadow-md p-12 text-center">
          <p className="text-gray-600 mb-4">No projects yet. Create your first project to get started!</p>
          <Link
            to="/projects/new"
            className="inline-block bg-primary-600 hover:bg-primary-700 text-white px-6 py-3 rounded-md font-medium"
          >
            Create Project
          </Link>
        </div>
      ) : (
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
          {projects.map((project) => (
            <Link
              key={project.id}
              to={`/projects/${project.id}`}
              className="bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow p-6 border border-gray-200"
            >
              <h2 className="text-xl font-semibold text-gray-900 mb-2">{project.name}</h2>
              <p className="text-sm text-gray-600 mb-4">{project.website_url}</p>
              <div className="flex justify-between items-center text-sm text-gray-500">
                <span>{project.content_count} content pieces</span>
                <span>{new Date(project.updated_at).toLocaleDateString()}</span>
              </div>
            </Link>
          ))}
        </div>
      )}
    </div>
  )
}
