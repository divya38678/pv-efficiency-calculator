Dashboard::::::::
"use client"

import { Button } from "../../components/ui/button"

export default function Dashboard({ onGoToQueue, onGoToFinished }) {
  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-orange-50">
      {/* Header */}
      <header className="bg-white border-b border-gray-200 px-6 py-4 shadow-sm">
        <div className="flex items-center justify-center">
          <div className="flex items-center space-x-12">
            <div className="w-10 h-10 bg-gradient-to-r from-blue-500 to-blue-600 rounded-full flex items-center justify-center">
              <span className="text-white font-bold text-sm">OPS</span>
            </div>
            <nav className="flex space-x-12">
              <span className="text-blue-600 font-semibold border-b-2 border-blue-600 pb-1">DASHBOARD</span>
              <button onClick={onGoToQueue} className="text-gray-700 font-medium hover:text-blue-600 transition-colors">
                WORK QUEUE
              </button>
              <button
                onClick={onGoToFinished}
                className="text-gray-700 font-medium hover:text-blue-600 transition-colors"
              >
                FINISHED TASKS
              </button>
              <span className="text-gray-700 font-medium hover:text-blue-600 cursor-pointer transition-colors">
                REPORTS
              </span>
              <span className="text-gray-700 font-medium hover:text-blue-600 cursor-pointer transition-colors">
                HELP
              </span>
              <span className="text-gray-700 font-medium hover:text-blue-600 cursor-pointer transition-colors">
                NOTIFICATIONS
              </span>
            </nav>
            <div className="w-8 h-8 bg-gradient-to-r from-orange-400 to-orange-500 rounded-full flex items-center justify-center">
              <span className="text-white font-bold text-xs">JD</span>
            </div>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="p-8">
        <div className="max-w-6xl mx-auto">
          <h1 className="text-3xl font-bold text-center mb-12 text-gray-800">Operations Dashboard</h1>

          {/* Stats Cards */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mb-12">
            <div className="bg-white rounded-xl shadow-lg p-6 border-l-4 border-blue-500">
              <h3 className="text-lg font-semibold text-gray-700 mb-2">Pending Tasks</h3>
              <p className="text-3xl font-bold text-blue-600">12</p>
            </div>
            <div className="bg-white rounded-xl shadow-lg p-6 border-l-4 border-orange-500">
              <h3 className="text-lg font-semibold text-gray-700 mb-2">In Progress</h3>
              <p className="text-3xl font-bold text-orange-600">5</p>
            </div>
            <div className="bg-white rounded-xl shadow-lg p-6 border-l-4 border-green-500">
              <h3 className="text-lg font-semibold text-gray-700 mb-2">Completed Today</h3>
              <p className="text-3xl font-bold text-green-600">8</p>
            </div>
          </div>

          {/* Quick Actions */}
          <div className="bg-white rounded-xl shadow-lg p-8">
            <h2 className="text-xl font-semibold text-gray-800 mb-6">Quick Actions</h2>
            <div className="flex flex-wrap gap-4">
              <Button
                onClick={onGoToQueue}
                className="bg-gradient-to-r from-blue-500 to-blue-600 hover:from-blue-600 hover:to-blue-700 text-white px-6 py-3 rounded-lg font-medium"
              >
                View Work Queue
              </Button>
              <Button
                onClick={onGoToFinished}
                className="bg-gradient-to-r from-orange-500 to-orange-600 hover:from-orange-600 hover:to-orange-700 text-white px-6 py-3 rounded-lg font-medium"
              >
                View Finished Tasks
              </Button>
              <Button className="bg-gradient-to-r from-gray-500 to-gray-600 hover:from-gray-600 hover:to-gray-700 text-white px-6 py-3 rounded-lg font-medium">
                Generate Report
              </Button>
            </div>
          </div>
        </div>
      </main>
    </div>
  )
}

FinishedTasks::::::::
"use client"

import { Button } from "../../components/ui/button"

export default function FinishedTasks({ onGoToDashboard, onGoToQueue }) {
  const finishedTasks = [
    {
      workId: "WRK001",
      submittedBy: "John Doe",
      submissionDate: "2024-01-15",
      completedDate: "2024-01-16",
      status: "Approved",
      checkedBy: "Jane Checker",
    },
    {
      workId: "WRK002",
      submittedBy: "Alice Smith",
      submissionDate: "2024-01-14",
      completedDate: "2024-01-15",
      status: "Rejected",
      checkedBy: "Mike Checker",
    },
    {
      workId: "WRK003",
      submittedBy: "Bob Johnson",
      submissionDate: "2024-01-13",
      completedDate: "2024-01-14",
      status: "Approved",
      checkedBy: "Sarah Checker",
    },
  ]

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-orange-50">
      {/* Header */}
      <header className="bg-white border-b border-gray-200 px-6 py-4 shadow-sm">
        <div className="flex items-center justify-center">
          <div className="flex items-center space-x-12">
            <div className="w-10 h-10 bg-gradient-to-r from-blue-500 to-blue-600 rounded-full flex items-center justify-center">
              <span className="text-white font-bold text-sm">OPS</span>
            </div>
            <nav className="flex space-x-12">
              <button
                onClick={onGoToDashboard}
                className="text-gray-700 font-medium hover:text-blue-600 transition-colors"
              >
                DASHBOARD
              </button>
              <button onClick={onGoToQueue} className="text-gray-700 font-medium hover:text-blue-600 transition-colors">
                WORK QUEUE
              </button>
              <span className="text-blue-600 font-semibold border-b-2 border-blue-600 pb-1">FINISHED TASKS</span>
              <span className="text-gray-700 font-medium hover:text-blue-600 cursor-pointer transition-colors">
                REPORTS
              </span>
              <span className="text-gray-700 font-medium hover:text-blue-600 cursor-pointer transition-colors">
                HELP
              </span>
              <span className="text-gray-700 font-medium hover:text-blue-600 cursor-pointer transition-colors">
                NOTIFICATIONS
              </span>
            </nav>
            <div className="w-8 h-8 bg-gradient-to-r from-orange-400 to-orange-500 rounded-full flex items-center justify-center">
              <span className="text-white font-bold text-xs">JD</span>
            </div>
          </div>
        </div>
      </header>

      {/* Sidebar */}
      <div className="flex">
        <aside className="w-16 bg-gradient-to-b from-blue-100 to-orange-100 min-h-screen flex flex-col items-center py-6 space-y-6">
          <div className="w-6 h-6 border-2 border-blue-500 rounded bg-blue-50"></div>
          <div className="w-6 h-6 flex items-center justify-center">
            <div className="w-4 h-0.5 bg-orange-500"></div>
            <div className="w-0.5 h-4 bg-orange-500 absolute"></div>
          </div>
        </aside>

        {/* Main Content */}
        <main className="flex-1 p-8">
          <div className="max-w-6xl mx-auto">
            <h1 className="text-3xl font-bold text-center mb-8 text-gray-800">FINISHED TASKS</h1>

            {/* Tasks Table */}
            <div className="bg-white rounded-xl shadow-lg border border-gray-200 overflow-hidden">
              <div className="bg-gradient-to-r from-green-500 to-green-600 px-6 py-4">
                <div className="grid grid-cols-7 gap-4 font-semibold text-white">
                  <div>WORK ID</div>
                  <div>SUBMITTED BY</div>
                  <div>SUBMISSION DATE</div>
                  <div>COMPLETED DATE</div>
                  <div>STATUS</div>
                  <div>CHECKED BY</div>
                  <div>ACTION</div>
                </div>
              </div>

              <div className="divide-y divide-gray-200">
                {finishedTasks.map((task, index) => (
                  <div
                    key={task.workId}
                    className={`px-6 py-4 ${index % 2 === 0 ? "bg-gray-50" : "bg-white"} hover:bg-green-50 transition-colors`}
                  >
                    <div className="grid grid-cols-7 gap-4 items-center">
                      <div className="text-gray-800 font-medium">{task.workId}</div>
                      <div className="text-gray-700">{task.submittedBy}</div>
                      <div className="text-gray-700">{task.submissionDate}</div>
                      <div className="text-gray-700">{task.completedDate}</div>
                      <div>
                        <span
                          className={`px-3 py-1 rounded-full text-xs font-medium ${
                            task.status === "Approved" ? "bg-green-100 text-green-800" : "bg-red-100 text-red-800"
                          }`}
                        >
                          {task.status}
                        </span>
                      </div>
                      <div className="text-gray-700">{task.checkedBy}</div>
                      <div>
                        <Button className="bg-gradient-to-r from-blue-500 to-blue-600 hover:from-blue-600 hover:to-blue-700 text-white px-4 py-2 rounded-lg font-medium text-sm">
                          VIEW DETAILS
                        </Button>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </div>

            {/* Summary Stats */}
            <div className="mt-8 grid grid-cols-1 md:grid-cols-3 gap-6">
              <div className="bg-white rounded-xl shadow-lg p-6 border-l-4 border-green-500">
                <h3 className="text-lg font-semibold text-gray-700 mb-2">Total Approved</h3>
                <p className="text-3xl font-bold text-green-600">2</p>
              </div>
              <div className="bg-white rounded-xl shadow-lg p-6 border-l-4 border-red-500">
                <h3 className="text-lg font-semibold text-gray-700 mb-2">Total Rejected</h3>
                <p className="text-3xl font-bold text-red-600">1</p>
              </div>
              <div className="bg-white rounded-xl shadow-lg p-6 border-l-4 border-blue-500">
                <h3 className="text-lg font-semibold text-gray-700 mb-2">Total Processed</h3>
                <p className="text-3xl font-bold text-blue-600">3</p>
              </div>
            </div>
          </div>
        </main>
      </div>
    </div>
  )
                             }
                             WorkItemDetails:::::
                             "use client"

import { Button } from "../../components/ui/button"

export default function FinishedTasks({ onGoToDashboard, onGoToQueue }) {
  const finishedTasks = [
    {
      workId: "WRK001",
      submittedBy: "John Doe",
      submissionDate: "2024-01-15",
      completedDate: "2024-01-16",
      status: "Approved",
      checkedBy: "Jane Checker",
    },
    {
      workId: "WRK002",
      submittedBy: "Alice Smith",
      submissionDate: "2024-01-14",
      completedDate: "2024-01-15",
      status: "Rejected",
      checkedBy: "Mike Checker",
    },
    {
      workId: "WRK003",
      submittedBy: "Bob Johnson",
      submissionDate: "2024-01-13",
      completedDate: "2024-01-14",
      status: "Approved",
      checkedBy: "Sarah Checker",
    },
  ]

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-orange-50">
      {/* Header */}
      <header className="bg-white border-b border-gray-200 px-6 py-4 shadow-sm">
        <div className="flex items-center justify-center">
          <div className="flex items-center space-x-12">
            <div className="w-10 h-10 bg-gradient-to-r from-blue-500 to-blue-600 rounded-full flex items-center justify-center">
              <span className="text-white font-bold text-sm">OPS</span>
            </div>
            <nav className="flex space-x-12">
              <button
                onClick={onGoToDashboard}
                className="text-gray-700 font-medium hover:text-blue-600 transition-colors"
              >
                DASHBOARD
              </button>
              <button onClick={onGoToQueue} className="text-gray-700 font-medium hover:text-blue-600 transition-colors">
                WORK QUEUE
              </button>
              <span className="text-blue-600 font-semibold border-b-2 border-blue-600 pb-1">FINISHED TASKS</span>
              <span className="text-gray-700 font-medium hover:text-blue-600 cursor-pointer transition-colors">
                REPORTS
              </span>
              <span className="text-gray-700 font-medium hover:text-blue-600 cursor-pointer transition-colors">
                HELP
              </span>
              <span className="text-gray-700 font-medium hover:text-blue-600 cursor-pointer transition-colors">
                NOTIFICATIONS
              </span>
            </nav>
            <div className="w-8 h-8 bg-gradient-to-r from-orange-400 to-orange-500 rounded-full flex items-center justify-center">
              <span className="text-white font-bold text-xs">JD</span>
            </div>
          </div>
        </div>
      </header>

      {/* Sidebar */}
      <div className="flex">
        <aside className="w-16 bg-gradient-to-b from-blue-100 to-orange-100 min-h-screen flex flex-col items-center py-6 space-y-6">
          <div className="w-6 h-6 border-2 border-blue-500 rounded bg-blue-50"></div>
          <div className="w-6 h-6 flex items-center justify-center">
            <div className="w-4 h-0.5 bg-orange-500"></div>
            <div className="w-0.5 h-4 bg-orange-500 absolute"></div>
          </div>
        </aside>

        {/* Main Content */}
        <main className="flex-1 p-8">
          <div className="max-w-6xl mx-auto">
            <h1 className="text-3xl font-bold text-center mb-8 text-gray-800">FINISHED TASKS</h1>

            {/* Tasks Table */}
            <div className="bg-white rounded-xl shadow-lg border border-gray-200 overflow-hidden">
              <div className="bg-gradient-to-r from-green-500 to-green-600 px-6 py-4">
                <div className="grid grid-cols-7 gap-4 font-semibold text-white">
                  <div>WORK ID</div>
                  <div>SUBMITTED BY</div>
                  <div>SUBMISSION DATE</div>
                  <div>COMPLETED DATE</div>
                  <div>STATUS</div>
                  <div>CHECKED BY</div>
                  <div>ACTION</div>
                </div>
              </div>

              <div className="divide-y divide-gray-200">
                {finishedTasks.map((task, index) => (
                  <div
                    key={task.workId}
                    className={`px-6 py-4 ${index % 2 === 0 ? "bg-gray-50" : "bg-white"} hover:bg-green-50 transition-colors`}
                  >
                    <div className="grid grid-cols-7 gap-4 items-center">
                      <div className="text-gray-800 font-medium">{task.workId}</div>
                      <div className="text-gray-700">{task.submittedBy}</div>
                      <div className="text-gray-700">{task.submissionDate}</div>
                      <div className="text-gray-700">{task.completedDate}</div>
                      <div>
                        <span
                          className={`px-3 py-1 rounded-full text-xs font-medium ${
                            task.status === "Approved" ? "bg-green-100 text-green-800" : "bg-red-100 text-red-800"
                          }`}
                        >
                          {task.status}
                        </span>
                      </div>
                      <div className="text-gray-700">{task.checkedBy}</div>
                      <div>
                        <Button className="bg-gradient-to-r from-blue-500 to-blue-600 hover:from-blue-600 hover:to-blue-700 text-white px-4 py-2 rounded-lg font-medium text-sm">
                          VIEW DETAILS
                        </Button>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </div>

            {/* Summary Stats */}
            <div className="mt-8 grid grid-cols-1 md:grid-cols-3 gap-6">
              <div className="bg-white rounded-xl shadow-lg p-6 border-l-4 border-green-500">
                <h3 className="text-lg font-semibold text-gray-700 mb-2">Total Approved</h3>
                <p className="text-3xl font-bold text-green-600">2</p>
              </div>
              <div className="bg-white rounded-xl shadow-lg p-6 border-l-4 border-red-500">
                <h3 className="text-lg font-semibold text-gray-700 mb-2">Total Rejected</h3>
                <p className="text-3xl font-bold text-red-600">1</p>
              </div>
              <div className="bg-white rounded-xl shadow-lg p-6 border-l-4 border-blue-500">
                <h3 className="text-lg font-semibold text-gray-700 mb-2">Total Processed</h3>
                <p className="text-3xl font-bold text-blue-600">3</p>
              </div>
            </div>
          </div>
        </main>
      </div>
    </div>
  )
}

                WorkQueue:::::
                            "use client"

import { Button } from "../../components/ui/button"
import { useState } from "react"

export default function WorkQueue({ onViewDetails, onGoToDashboard, onGoToFinished }) {
  const [workIdFilter, setWorkIdFilter] = useState("")
  const [nameFilter, setNameFilter] = useState("")
  const [dateFilter, setDateFilter] = useState("")

  const mockTasks = [
    {
      workId: "WRK001",
      submittedBy: "John Doe",
      submissionDate: "2024-01-15",
      status: "Pending Review",
    },
    {
      workId: "WRK002",
      submittedBy: "Jane Smith",
      submissionDate: "2024-01-16",
      status: "In Progress",
    },
    {
      workId: "WRK003",
      submittedBy: "Mike Johnson",
      submissionDate: "2024-01-17",
      status: "Pending Review",
    },
  ]

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-orange-50">
      {/* Header */}
      <header className="bg-white border-b border-gray-200 px-6 py-4 shadow-sm">
        <div className="flex items-center justify-center">
          <div className="flex items-center space-x-12">
            <div className="w-10 h-10 bg-gradient-to-r from-blue-500 to-blue-600 rounded-full flex items-center justify-center">
              <span className="text-white font-bold text-sm">OPS</span>
            </div>
            <nav className="flex space-x-12">
              <button
                onClick={onGoToDashboard}
                className="text-gray-700 font-medium hover:text-blue-600 transition-colors"
              >
                DASHBOARD
              </button>
              <span className="text-blue-600 font-semibold border-b-2 border-blue-600 pb-1">WORK QUEUE</span>
              <button
                onClick={onGoToFinished}
                className="text-gray-700 font-medium hover:text-blue-600 cursor-pointer transition-colors"
              >
                FINISHED TASKS
              </button>
              <span className="text-gray-700 font-medium hover:text-blue-600 cursor-pointer transition-colors">
                REPORTS
              </span>
              <span className="text-gray-700 font-medium hover:text-blue-600 cursor-pointer transition-colors">
                HELP
              </span>
              <span className="text-gray-700 font-medium hover:text-blue-600 cursor-pointer transition-colors">
                NOTIFICATIONS
              </span>
            </nav>
            <div className="w-8 h-8 bg-gradient-to-r from-orange-400 to-orange-500 rounded-full flex items-center justify-center">
              <span className="text-white font-bold text-xs">JD</span>
            </div>
          </div>
        </div>
      </header>

      {/* Sidebar */}
      <div className="flex">
        <aside className="w-16 bg-gradient-to-b from-blue-100 to-orange-100 min-h-screen flex flex-col items-center py-6 space-y-6">
          <div className="w-6 h-6 border-2 border-blue-500 rounded bg-blue-50"></div>
          <div className="w-6 h-6 flex items-center justify-center">
            <div className="w-4 h-0.5 bg-orange-500"></div>
            <div className="w-0.5 h-4 bg-orange-500 absolute"></div>
          </div>
        </aside>

        {/* Main Content */}
        <main className="flex-1 p-8">
          <div className="max-w-6xl mx-auto">
            <h1 className="text-3xl font-bold text-center mb-8 text-gray-800">ASSIGNED TASKS</h1>

            {/* Tasks Table */}
            <div className="bg-white rounded-xl shadow-lg border border-gray-200 overflow-hidden mb-8">
              <div className="bg-gradient-to-r from-blue-500 to-blue-600 px-6 py-4">
                <div className="grid grid-cols-6 gap-4 font-semibold text-white">
                  <div>WORK ID</div>
                  <div>SUBMITTED BY</div>
                  <div>SUBMISSION DATE</div>
                  <div>STATUS</div>
                  <div>ACTION</div>
                  <div></div>
                </div>
              </div>

              <div className="divide-y divide-gray-200">
                {mockTasks.map((task, index) => (
                  <div
                    key={task.workId}
                    className={`px-6 py-4 ${index % 2 === 0 ? "bg-gray-50" : "bg-white"} hover:bg-blue-50 transition-colors`}
                  >
                    <div className="grid grid-cols-6 gap-4 items-center">
                      <div className="text-gray-800 font-medium">{task.workId}</div>
                      <div className="text-gray-700">{task.submittedBy}</div>
                      <div className="text-gray-700">{task.submissionDate}</div>
                      <div>
                        <span
                          className={`px-3 py-1 rounded-full text-xs font-medium ${
                            task.status === "Pending Review"
                              ? "bg-orange-100 text-orange-800"
                              : "bg-blue-100 text-blue-800"
                          }`}
                        >
                          {task.status}
                        </span>
                      </div>
                      <div>
                        <Button
                          onClick={() => onViewDetails(task.workId)}
                          className="bg-gradient-to-r from-orange-500 to-orange-600 hover:from-orange-600 hover:to-orange-700 text-white px-6 py-2 rounded-lg font-medium"
                        >
                          VIEW
                        </Button>
                      </div>
                      <div></div>
                    </div>
                  </div>
                ))}
              </div>
            </div>

            {/* Filter Section */}
            <div className="bg-white rounded-xl shadow-lg p-6">
              <h3 className="text-lg font-semibold text-gray-800 mb-4">FILTER BY:</h3>
              <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">Work ID</label>
                  <input
                    type="text"
                    value={workIdFilter}
                    onChange={(e) => setWorkIdFilter(e.target.value)}
                    placeholder="Enter Work ID"
                    className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">Name</label>
                  <input
                    type="text"
                    value={nameFilter}
                    onChange={(e) => setNameFilter(e.target.value)}
                    placeholder="Enter Name"
                    className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">Date</label>
                  <input
                    type="date"
                    value={dateFilter}
                    onChange={(e) => setDateFilter(e.target.value)}
                    className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                  />
                </div>
              </div>
              <div className="mt-4 flex gap-3">
                <Button className="bg-gradient-to-r from-blue-500 to-blue-600 hover:from-blue-600 hover:to-blue-700 text-white px-6 py-2 rounded-lg">
                  Apply Filters
                </Button>
                <Button
                  onClick={() => {
                    setWorkIdFilter("")
                    setNameFilter("")
                    setDateFilter("")
                  }}
                  className="bg-gray-500 hover:bg-gray-600 text-white px-6 py-2 rounded-lg"
                >
                  Clear
                </Button>
              </div>
            </div>
          </div>
        </main>
      </div>
    </div>
  )
}

                           app.js:::::::
                           "use client"

import { useState } from "react"
import Dashboard from "./components/Dashboard"
import WorkQueue from "./components/WorkQueue"
import WorkItemDetails from "./components/WorkItemDetails"
import FinishedTasks from "./components/FinishedTasks"

function App() {
  const [currentView, setCurrentView] = useState("dashboard")
  const [selectedWorkItem, setSelectedWorkItem] = useState(null)

  const handleGoToDashboard = () => setCurrentView("dashboard")
  const handleGoToQueue = () => setCurrentView("workQueue")
  const handleGoToFinished = () => setCurrentView("finishedTasks")

  const handleViewDetails = (workId) => {
    setSelectedWorkItem(workId)
    setCurrentView("workItemDetails")
  }

  const handleApprove = () => {
    setCurrentView("finishedTasks")
  }

  const renderCurrentView = () => {
    switch (currentView) {
      case "dashboard":
        return <Dashboard onGoToQueue={handleGoToQueue} onGoToFinished={handleGoToFinished} />
      case "workQueue":
        return (
          <WorkQueue
            onViewDetails={handleViewDetails}
            onGoToDashboard={handleGoToDashboard}
            onGoToFinished={handleGoToFinished}
          />
        )
      case "workItemDetails":
        return (
          <WorkItemDetails
            workId={selectedWorkItem}
            onBackToQueue={handleGoToQueue}
            onGoToDashboard={handleGoToDashboard}
            onGoToFinished={handleGoToFinished}
            onApprove={handleApprove}
          />
        )
      case "finishedTasks":
        return <FinishedTasks onGoToDashboard={handleGoToDashboard} onGoToQueue={handleGoToQueue} />
      default:
        return <Dashboard onGoToQueue={handleGoToQueue} onGoToFinished={handleGoToFinished} />
    }
  }

  return <div className="min-h-screen bg-gray-50">{renderCurrentView()}</div>
}

export default App

                             

















app:::
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './components/Navbar';
import CustomersList from './pages/CustomersList';
import CustomerDetails from './pages/CustomerDetails';
import CustomerForm from './pages/CustomerForm';

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <Routes>
          <Route path="/customers" element={<CustomersList />} />
          <Route path="/customers/:id" element={<CustomerDetails />} />
          <Route path="/add-customer" element={<CustomerForm />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;

cf:
import React, { useState } from 'react';

const CustomerForm = () => {
  const [formData, setFormData] = useState({
    firstName: '',
    lastName: '',
    email: '',
    phone: '',
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Validate form data
    if (!formData.firstName || !formData.lastName || !formData.email || !formData.phone) {
      alert('All fields are required.');
      return;
    }
    // Simulate form submission
    console.log('Form submitted:', formData);
    // Redirect to customer list page
    window.location.href = '/customers';
  };

  return (
    <div>
      <h2>Add Customer</h2>
      <form onSubmit={handleSubmit}>
        <label>
          First Name:
          <input
            type="text"
            name="firstName"
            value={formData.firstName}
            onChange={handleChange}
            placeholder="Please enter first name"
          />
        </label>
        <br />
        <label>
          Last Name:
          <input
            type="text"
            name="lastName"
            value={formData.lastName}
            onChange={handleChange}
            placeholder="Please enter last name"
          />
        </label>
        <br />
        <label>
          Email:
          <input
            type="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            placeholder="Please enter email details"
          />
        </label>
        <br />
        <label>
          Phone:
          <input
            type="tel"
            name="phone"
            value={formData.phone}
            onChange={handleChange}
            placeholder="Please enter phone no"
          />
        </label>
        <br />
        <button type="submit">Create Customer</button>
      </form>
    </div>
  );
};

export default CustomerForm;

cd::
import React from 'react';
import { useParams } from 'react-router-dom';

const CustomerDetails = () => {
  const { id } = useParams();
  const customer = {
    id: 1,
    firstName: 'Sundar',
    lastName: 'Pichai',
    email: 'sundar.pichai@google.com',
    phone: '1234567890',
    accounts: [
      { accountNo: '1001999', type: 'SAVINGS_ACCOUNT', branch: 'Bellandur', balance: 1000 },
      { accountNo: '1001888', type: 'SAVINGS_ACCOUNT', branch: 'Indira Nagar', balance: 2000 },
    ],
  };

  return (
    <div>
      <h2>Customer Details</h2>
      <p>ID: {customer.id}</p>
      <p>First Name: {customer.firstName}</p>
      <p>Last Name: {customer.lastName}</p>
      <p>Email: {customer.email}</p>
      <p>Phone: {customer.phone}</p>

      <h3>List of Accounts</h3>
      <table>
        <thead>
          <tr>
            <th>Account No</th>
            <th>Type</th>
            <th>Branch</th>
            <th>Balance</th>
          </tr>
        </thead>
        <tbody>
          {customer.accounts.map(account => (
            <tr key={account.accountNo}>
              <td>{account.accountNo}</td>
              <td>{account.type}</td>
              <td>{account.branch}</td>
              <td>{account.balance}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default CustomerDetails;

cl:::
import React from 'react';
import { Link } from 'react-router-dom';

const CustomersList = () => {
  const customers = [
    { id: 1, firstName: 'Sundar', lastName: 'Pichai', email: 'sundar.pichai@google.com' },
    { id: 2, firstName: 'Jeff', lastName: 'Bezos', email: 'jeff.bezos@amazon.com' },
    // Add more customers as needed
  ];

  return (
    <div>
      <h2>Customers List</h2>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>First Name</th>
            <th>Last Name</th>
            <th>Email</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {customers.map(customer => (
            <tr key={customer.id}>
              <td>{customer.id}</td>
              <td>{customer.firstName}</td>
              <td>{customer.lastName}</td>
              <td>{customer.email}</td>
              <td>
                <Link to={`/customers/${customer.id}`}>Show</Link>
                <button>Edit</button>
                <button>Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default CustomersList;



import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# Set page config
st.set_page_config(page_title="PV Efficiency Calculator", page_icon="☀️")

# App title
st.title("☀️ PV System Efficiency Calculator")
st.markdown("Estimate your solar panel system's efficiency and download reports!")

# First efficiency calculator based on energy
st.header("📊 Input System Parameters (kWh-based)")

solar_input = st.number_input("Total solar energy received (kWh)", min_value=0.0)
output_energy = st.number_input("Output energy from PV system (kWh)", min_value=0.0)

if solar_input > 0:
    efficiency = (output_energy / solar_input) * 100
    st.success(f"✅ Efficiency = {efficiency:.2f}%")
else:
    st.warning("⚠️ Please enter a valid solar input.")

# Plot simulated efficiency data
st.header("📈 Efficiency Over Time (Sample Data)")

days = list(range(1, 8))
efficiency_data = [70, 72, 68, 74, 69, 71, 73]

fig, ax = plt.subplots()
ax.plot(days, efficiency_data, marker='o', color='orange')
ax.set_xlabel("Day")
ax.set_ylabel("Efficiency (%)")
ax.set_title("Weekly PV System Efficiency")

st.pyplot(fig)

# Second efficiency calculator based on panel area and irradiance
st.header("🔧 Panel-Based Efficiency Calculator (W/m²)")

def calculate_pv_efficiency(area_m2, irradiance_w_m2, output_power_w):
    input_power = irradiance_w_m2 * area_m2
    if input_power == 0:
        return 0
    efficiency = (output_power_w / input_power) * 100
    return round(efficiency, 2)

area = st.number_input("Solar Panel Area (in m²)", min_value=0.1, value=1.6, step=0.1)
irradiance = st.number_input("Solar Irradiance (in W/m²)", min_value=100, value=1000, step=50)
output_power = st.number_input("Output Power (in W)", min_value=1, value=280, step=10)

if st.button("Calculate Efficiency"):
    efficiency = calculate_pv_efficiency(area, irradiance, output_power)
    st.success(f"⚡ Efficiency: {efficiency}%")
    st.progress(min(int(efficiency), 100))

# CSV export
st.markdown("---")
st.header("📥 Download Efficiency Data")

df = pd.DataFrame({
    "Day": days,
    "Efficiency (%)": efficiency_data
})
st.dataframe(df)

csv = df.to_csv(index=False).encode('utf-8')

import React, { useState } from 'react';
import './Login.css'; // reusing same styles

const Register = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleRegister = (e) => {
    e.preventDefault();
    console.log("Registering:", { username, password });
    // Add your registration logic here (API call etc.)
  };

  return (
    <div className="login-container">
      <h2>Register</h2>
      <input
        type="text"
        placeholder="Username"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />
      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      <button onClick={handleRegister}>Register</button>
    </div>
  );
};

export default Register;

/* Login.css */

.login-container {
  width: 300px;
  margin: 100px auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  background-color: #fff;
}

.login-container h2 {
  text-align: center;
  margin-bottom: 20px;
}

.login-container input {
  width: 100%;
  padding: 10px;
  margin: 10px 0;
  border-radius: 4px;
  border: 1px solid #ccc;
}

.login-container button {
  width: 100%;
  padding: 10px;
  background-color: #007bff;
  border: none;
  color: white;
  font-weight: bold;
  border-radius: 4px;
  cursor: pointer;
}

.login-container button:hover {
  background-color: #0056b3;
}
This is the Checkers page for User Story 4. 
At the top, we’ve got a clean navigation bar with quick links, notifications,
and messages so users can access everything without leaving the page. 
The main section is focused on displaying checkers’ tasks and updates 
in a clear, scrollable layout, with options to take action quickly. 
The design keeps the workflow intuitive while making sure important 
information is always visible

This is the Checkers page for User Story 4, designed to let users 
quickly review applicant details and verify documents. The top section
is neatly organized into personal, employment, and loan details for quick
reference. The right panel serves as a document viewer where checkers 
can preview files like Aadhaar and photographs side by side, streamlining the verification process.




st.download_button("⬇️ Download CSV", csv, "efficiency_data.csv", "text/csv")

st.caption("Built with ❤️ using Streamlit")














