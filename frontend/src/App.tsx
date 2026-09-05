import { NavLink, Route, Routes } from 'react-router-dom'
import { ContentDetailPage } from './features/content/ContentDetailPage'
import { ContentExplorerPage } from './features/content/ContentExplorerPage'
import { DashboardPage } from './features/dashboard/DashboardPage'
import { LifeHubPage } from './features/life/LifeHubPage'
import { LifeSkillPage } from './features/life/LifeSkillPage'
import { PromptPage } from './features/prompt-bridge/PromptPage'
import { ProjectDetailPage } from './features/projects/ProjectDetailPage'
import { ProjectListPage } from './features/projects/ProjectListPage'
import { WeeklyPage } from './features/weekly/WeeklyPage'
import { SettingsPage } from './features/settings/SettingsPage'

const navItems = [
  ['/', '대시보드'],
  ['/weekly', '이번 주'],
  ['/content', '콘텐츠'],
  ['/life', '생활'],
  ['/projects', '프로젝트'],
  ['/prompt', 'Prompt Bridge'],
  ['/settings', '설정/백업'],
] as const

export default function App() {
  return (
    <div className="app-shell">
      <aside className="sidebar">
        <div className="brand"><span>BDO</span> Companion</div>
        <p className="eyebrow">LOCAL OPERATIONS</p>
        <nav>
          {navItems.map(([to, label]) => (
            <NavLink key={to} to={to} end={to === '/'}>{label}</NavLink>
          ))}
        </nav>
        <div className="local-note">외부 AI 연결 없음<br />데이터는 이 PC에 보관됩니다.</div>
      </aside>
      <main className="main-content">
        <Routes>
          <Route path="/" element={<DashboardPage />} />
          <Route path="/weekly" element={<WeeklyPage />} />
          <Route path="/content" element={<ContentExplorerPage />} />
          <Route path="/content/:slug" element={<ContentDetailPage />} />
          <Route path="/life" element={<LifeHubPage />} />
          <Route path="/life/:skill" element={<LifeSkillPage />} />
          <Route path="/projects" element={<ProjectListPage />} />
          <Route path="/projects/:slug" element={<ProjectDetailPage />} />
          <Route path="/prompt" element={<PromptPage />} />
          <Route path="/settings" element={<SettingsPage />} />
        </Routes>
      </main>
    </div>
  )
}
