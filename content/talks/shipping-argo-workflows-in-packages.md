---
title: "Shipping Argo Workflows in Packages 📦 - KubeCon 2023"
date: "2023-04-18"
toc: false
readTime: true
autonumber: false
math: false
draft: false
---

Presented in person at [ArgoCon 2023 hosted w/ KubeCon Europe 2023 in Amsterdam](https://colocatedeventseu2023.sched.com/type/ArgoCon).

## Links

- **Slides**: https://pitch.com/public/d9727a69-e494-410d-a6e5-787069492ad3
- **Talk Recording**: https://www.youtube.com/watch?v=UbnlQkIjn-4
- **Repository**: https://github.com/atlanhq/argopm
- **Event**: (https://colocatedeventseu2023.sched.com/event/1JoAG/shipping-argo-workflows-in-packages-junaid-rahim-nitin-sutrave-atlan)

## Submitted CFP Application

#### Abstract

The team at Atlan is building a collaborative workspace for modern data teams that offers functionality like metadata cataloguing, governance and lineage amongst others. Ingesting metadata from various data sources using ETL pipelines is one of the core functionalities of Atlan's platform.

Argo workflows is the leading open-source tool to run DAG like workflows on k8s. Workloads in argo are declared as workflow templates, however, there is no tooling currently present in the ecosystem to use them as reusable modules. This is the problem that Atlan's engineers faced when building data pipelines on argo workflows.

In this talk, Junaid and Nitin will dive deep into how they've used open-source tools from the JS ecosystem to build a package manager for argo workflows and its use cases in a production setup that runs ~2.5k workflows every week and processes ~20M metadata assets for hundreds of customers.

You will learn how the team at Atlan built its marketplace of composable and reusable packages on top of argo workflows using Verdaccio, an open-source private NPM registry. You will learn about argopm, the package manager to manage workflow templates as JS packages which also supports adding configmaps, secrets and observability components like grafana dashboards into the package.

#### Benefits to the Ecosystem

Argo workflows is the go-to tool to run workflow DAGs on k8s. In argo workflows, it is possible to reference other workflow templates in the same cluster. However, it does not have the tooling to distribute and consume these workflow templates as reusable modules. Usually, these templates are declared in multiple YAML files and have to be manually applied to the cluster when making changes, doing this becomes very tedious with a growing number of templates

Projects like couler and hera are solutions to distribute workflows as python packages, but there is no option for teams looking for a more language-agnostic solution that does not lock them into an ecosystem.

argopm enables developers to manage workflow templates just like npm packages. This helps with dependencies, versioning and all the other benefits of a package ecosystem.

We propose this talk to present the community with the package ecosystem built using argopm at Atlan to distribute workflow templates as standard packages.

#### Is your presentation considered a case study?

Yes

#### Have you or anyone else given this presentation before?

No

#### CNCF-hosted Software

[argo-workflows](https://github.com/argoproj/argo-workflows/)

#### Open Source Projects

[Verdaccio](https://github.com/verdaccio/verdaccio), [argopm](https://github.com/atlanhq/argopm)
