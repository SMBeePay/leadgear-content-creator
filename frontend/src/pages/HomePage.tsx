import { Link } from 'react-router-dom'
import { useAuthStore } from '../stores/authStore'

export default function HomePage() {
  const { user } = useAuthStore()

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <div className="text-center mb-12">
        <h1 className="text-4xl font-bold text-gray-900 mb-4">
          Welcome back, {user?.full_name || user?.email}!
        </h1>
        <p className="text-xl text-gray-600">
          Let's create some amazing content
        </p>
      </div>

      <div className="grid md:grid-cols-2 gap-8 max-w-4xl mx-auto">
        <Link
          to="/projects"
          className="bg-white p-8 rounded-lg shadow-md hover:shadow-lg transition-shadow border border-gray-200"
        >
          <div className="text-primary-600 mb-4">
            <svg className="w-12 h-12" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 7v10a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-6l-2-2H5a2 2 0 00-2 2z" />
            </svg>
          </div>
          <h2 className="text-2xl font-semibold text-gray-900 mb-2">My Projects</h2>
          <p className="text-gray-600">
            View and manage your client projects and content pieces
          </p>
        </Link>

        <div className="bg-white p-8 rounded-lg shadow-md border border-gray-200 opacity-60">
          <div className="text-gray-400 mb-4">
            <svg className="w-12 h-12" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
            </svg>
          </div>
          <h2 className="text-2xl font-semibold text-gray-400 mb-2">Analytics</h2>
          <p className="text-gray-400">
            Coming soon: Track content performance and ROI
          </p>
        </div>
      </div>

      <div className="mt-12 bg-primary-50 border border-primary-200 rounded-lg p-6 max-w-4xl mx-auto">
        <h3 className="text-lg font-semibold text-primary-900 mb-2">Quick Start Guide</h3>
        <ol className="list-decimal list-inside space-y-2 text-primary-800">
          <li>Create a new project for your client</li>
          <li>Start content creation with keyword research</li>
          <li>Review and approve AI-generated content brief</li>
          <li>Generate and edit your content draft</li>
          <li>Export to Google Docs for client delivery</li>
        </ol>
      </div>
    </div>
  )
}
