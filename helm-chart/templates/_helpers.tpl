{{/*
Create chart name and version as used by the chart label.
*/}}
{{- define "allure.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Common labels
*/}}
{{- define "allure.labels" -}}
helm.sh/chart: {{ include "allure.chart" . }}
app.kubernetes.io/part-of: allure-sample
{{ include "allure.selectorLabels" . }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{/*
Selector labels
*/}}
{{- define "allure.selectorLabels" -}}
app.kubernetes.io/name: {{ include "allure.chart" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}
