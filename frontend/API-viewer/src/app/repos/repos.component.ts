import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Owner } from '../owner';
import { Repo } from '../repo';
import { RepoService } from '../repo.service';

@Component({
  selector: 'app-repos',
  templateUrl: './repos.component.html',
  styleUrls: ['./repos.component.css']
})
export class ReposComponent implements OnInit {
  related!: Owner;
  orgSearch!: string;

  selectedRepo!: Repo;

  constructor(
    private route: ActivatedRoute,
    private repoService: RepoService
  ) { }

  getRelatedRepos(): void {
    let org = this.route.snapshot.paramMap.get('owner');
    if(!org) return;
    this.orgSearch = org;
    this.repoService.getOwner(org)
      .subscribe(rep => this.related = rep)
  }

  onSelect(repo: Repo): void {
    this.selectedRepo = repo;
  }

  ngOnInit(): void {
    this.getRelatedRepos();
  }

}
