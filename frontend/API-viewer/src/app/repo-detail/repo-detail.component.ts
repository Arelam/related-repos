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
  @Input() repo!: Repo | null;
  
  constructor(
    private route: ActivatedRoute,
    private repoService: RepoService
  ) { }

  ngOnInit(): void {
  }

  // User hide-able
  onClose(): void {
    this.repo = null;
  }

}
