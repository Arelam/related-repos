import { Repo } from './repo';

export interface Owner {
	name: string | null;
	repositories: Repo[];
}