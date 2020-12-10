import { Component, Input, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Repo } from '../repo';
import { RepoService } from '../repo.service';

@Component({
  selector: 'app-repo-detail',
  templateUrl: './repo-detail.component.html',
  styleUrls: ['./repo-detail.component.css']
})
export class RepoDetailComponent implements OnInit {
  @Input() repo!: Repo;
  //repo!: Repo;
  
  constructor(
    private route: ActivatedRoute,
    private repoService: RepoService
  ) { }

  ngOnInit(): void {
    this.getRepo();
  }

  getRepo(): void {
    const owner = this.route.snapshot.paramMap.get('owner');
    const name = this.route.snapshot.paramMap.get('name');
    if(!name || !owner) return;
    this.repoService.getRepo(owner, name)
      .subscribe(repo => this.repo = repo);
  }

}
