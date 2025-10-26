import { Routes } from '@angular/router';
import { Home } from './pages/home/home';
import { Login } from './pages/login/login';
import { Profile } from './pages/profile/profile';
import { Register } from './pages/register/register';
import { DryRun } from './pages/dry-run/dry-run';
import { CommitRun } from './pages/commit-run/commit-run';
import { FullLoad } from './pages/full-load/full-load';

export const routes: Routes = [
    {
        path: "",
        pathMatch: "full",
        redirectTo: "/home",
    },
    {
        path: 'home',
        component: Home,
    },
    {
        path: 'dry-run',
        component: DryRun,
    },
    {
        path: 'commit-run',
        component: CommitRun,
    },
    {
        path: 'full-load',
        component: FullLoad,
    },
    {
        path: 'login',
        component: Login,
    },
    {
        path: 'profile',
        component: Profile,
    },
    {
        path: 'register',
        component: Register,
    },
];
