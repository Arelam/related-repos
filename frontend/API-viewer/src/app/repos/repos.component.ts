import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Organization } from '../organization';
import { Repo } from '../repo';
import { RepoService } from '../repo.service';

@Component({
  selector: 'app-repos',
  templateUrl: './repos.component.html',
  styleUrls: ['./repos.component.css']
})
export class ReposComponent implements OnInit {
  related!: Organization;
  orgSearch!: string;

  selectedRepo!: Repo;

  constructor(
    private route: ActivatedRoute,
    private repoService: RepoService
  ) { }

  getRelatedRepos(): void {
    let org = this.route.snapshot.paramMap.get('organization');
    if(!org) return;
    this.orgSearch = org;
    this.repoService.getRelatedRepositories(org)
      .subscribe(rep => this.related = rep)
  }

  onSelect(repo: Repo): void {
    this.selectedRepo = repo;
  }

  ngOnInit(): void {
    this.getRelatedRepos();
  }

}
