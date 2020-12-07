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
  //repos!: Repo[];
  owner!: Owner;
  name!: string;

  selectedRepo!: Repo;

  constructor(
    private route: ActivatedRoute,
    private repoService: RepoService
  ) { }

  // getRepos(): void {
  //   this.repoService.getRepos()
  //     .subscribe(repos => this.repos = repos)
  //   //this.repos = this.repoService.getRepos();
  // }

  getOwner(): void {
    let org = this.route.snapshot.paramMap.get('owner');
    if(!org) return;
    this.name = org;
    this.repoService.getOwner(this.name)
      .subscribe(owner => this.owner = owner)
  }

  // onSelect(repo: Repo): void {
  //   this.selectedRepo = repo;
  // }

  ngOnInit(): void {
    this.getOwner();
  }

}
