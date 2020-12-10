import { Injectable } from '@angular/core';
import { Repo } from './repo';
import { REPOS } from './mock-repos';
import { Observable, of } from 'rxjs';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { catchError, map, tap } from 'rxjs/operators';
import { Organization } from './organization';

@Injectable({
  providedIn: 'root'
})
export class RepoService {

  private reposUrl = 'http://0.0.0.0:8000/';  // URL to web api

  constructor(
    private http: HttpClient
  ) { }

  getRelatedRepositories(org: string): Observable<Organization> {
    return this.http.get<Organization>(this.reposUrl + 'relatedRepositories/' + org)
    .pipe(
      catchError(this.handleError<Organization>('getRelatedRepositories'))
    );
  }

  getRepo(owner: string, name: string): Observable<Repo> {
    return this.http.get<Repo>(`${this.reposUrl}${owner}/${name}`)
    .pipe(
      catchError(this.handleError<Repo>('getRepo'))
    );
  }
  
  // test later
  getRepos(): Observable<Repo[]> {
    //return of(REPOS);
    const testr = this.http.get<Repo[]>(this.reposUrl);
    console.log(testr)
    return this.http.get<Repo[]>(this.reposUrl)
    .pipe(
      catchError(this.handleError<Repo[]>('getRepos', []))
    );
  }

  

  private handleError<T>(operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {
  
      // TODO: send the error to remote logging infrastructure
      console.error(error); // log to console instead
    
      // Let the app keep running by returning an empty result.
      return of(result as T);
    };
  }
}
