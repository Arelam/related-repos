import { Repo } from './repo';

export interface Organization {
	orgName: string | null;
	repositories: Repo[];
}