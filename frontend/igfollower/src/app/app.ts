import { Component, signal } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  protected readonly totalFollowers = signal(0);
  protected readonly totalFollowing = signal(0);
  protected readonly notFollowingBack = signal(0);
  protected readonly youDontFollowBack = signal(0);
  protected readonly mutualFollows = signal(0);
  protected readonly followBackRatio = signal(0);
  protected readonly sidebarOpen = signal(false);

  protected readonly followersFile = signal<File | null>(null);
  protected readonly followingFile = signal<File | null>(null);
  protected readonly loading = signal(false);
  protected readonly error = signal('');
  protected readonly analyzed = signal(false);

  protected readonly dragOverFollowers = signal(false);
  protected readonly dragOverFollowing = signal(false);

  toggleSidebar() {
    this.sidebarOpen.update(v => !v);
  }

  onFileSelect(event: Event, type: 'followers' | 'following') {
    const input = event.target as HTMLInputElement;
    if (input.files && input.files[0]) {
      if (type === 'followers') {
        this.followersFile.set(input.files[0]);
      } else {
        this.followingFile.set(input.files[0]);
      }
    }
  }

  onDragOver(event: DragEvent, type: 'followers' | 'following') {
    event.preventDefault();
    if (type === 'followers') {
      this.dragOverFollowers.set(true);
    } else {
      this.dragOverFollowing.set(true);
    }
  }

  onDragLeave(type: 'followers' | 'following') {
    if (type === 'followers') {
      this.dragOverFollowers.set(false);
    } else {
      this.dragOverFollowing.set(false);
    }
  }

  onDrop(event: DragEvent, type: 'followers' | 'following') {
    event.preventDefault();
    this.onDragLeave(type);
    if (event.dataTransfer?.files && event.dataTransfer.files[0]) {
      if (type === 'followers') {
        this.followersFile.set(event.dataTransfer.files[0]);
      } else {
        this.followingFile.set(event.dataTransfer.files[0]);
      }
    }
  }

  async analyze() {
    const followers = this.followersFile();
    const following = this.followingFile();
    if (!followers || !following) return;

    this.loading.set(true);
    this.error.set('');

    const formData = new FormData();
    formData.append('followers', followers);
    formData.append('following', following);

    try {
      const res = await fetch('http://localhost:8000/analyze', {
        method: 'POST',
        body: formData,
      });

      if (!res.ok) {
        const err = await res.json().catch(() => ({ detail: 'Server error' }));
        throw new Error(err.detail || 'Analysis failed');
      }

      const data = await res.json();
      this.totalFollowers.set(data.totalFollowers);
      this.totalFollowing.set(data.totalFollowing);
      this.notFollowingBack.set(data.notFollowingBack);
      this.youDontFollowBack.set(data.youDontFollowBack);
      this.mutualFollows.set(data.mutualFollows);
      this.followBackRatio.set(data.followBackRatio);
      this.analyzed.set(true);
    } catch (e: any) {
      this.error.set(e.message || 'Something went wrong');
    } finally {
      this.loading.set(false);
    }
  }
}
