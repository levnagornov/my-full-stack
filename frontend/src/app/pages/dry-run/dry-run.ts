import { Component } from '@angular/core';
import { TasksService } from '../../services/task.service';

@Component({
  selector: 'app-dry-run',
  imports: [],
  templateUrl: './dry-run.html',
  styleUrl: './dry-run.css'
})
export class DryRun {

  file!: File;
  
  // @Output() submitTask = new EventEmitter<FormData>();

  constructor(
    private readonly taskService: TasksService
  ) { }

  onFileChange(event: any) {
    this.file = event.target.files[0];
  }

  submit() {
    const fd = new FormData();
    fd.append('file', this.file);
    alert();
    // fd.append('report_type', this.reportType);
    // this.submitTask.emit(fd);
  }
}
